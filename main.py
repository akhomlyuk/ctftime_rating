import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from design import Ui_MainWindow
from functions import results_from_ctftime, event_information
import json


class Ctftime(QMainWindow):
    def __init__(self):
        super(Ctftime, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.results_to_textedit()
        self.event_info_to_text_edit()
        self.rating_formula()
        self.rating_spinbox_to_progressbar()

        self.ui.rating_progress.setMaximum(self.rating_formula())
        self.ui.rating_progress.setValue(self.ui.rating_spinbox.value())
        self.ui.best_team_points.valueChanged.connect(self.rating_formula)

        # self.ui.event_id.valueChanged.connect(self.results_to_textedit)
        self.ui.event_id.editingFinished.connect(self.event_info_to_text_edit)
        self.ui.event_id.editingFinished.connect(self.results_to_textedit)
        # self.ui.go_btn.clicked.connect(self.results_to_textedit)
        # self.ui.go_btn.clicked.connect(self.event_info_to_text_edit)

        self.ui.team_points.valueChanged.connect(self.rating_formula)
        self.ui.best_team_points.valueChanged.connect(self.rating_formula)
        self.ui.team_place.valueChanged.connect(self.rating_formula)
        self.ui.teams.valueChanged.connect(self.rating_formula)
        self.ui.weight.valueChanged.connect(self.rating_formula)

        # self.ui.textEdit.setText(results_from_ctftime()[str(self.ui.event_id.value())]['scores'][0]['points'])

    def event_info_to_text_edit(self):
        try:
            event_info = event_information(self.ui.event_id.value())
            self.ui.event_info_text.setText(json.dumps(event_info, indent=4))
            self.ui.statusBar.clearMessage()
        except (KeyError, json.decoder.JSONDecodeError):
            self.ui.event_info_text.clear()
            self.ui.event_info_text.setText('Information not available')

    def results_to_textedit(self):
        try:
            result = results_from_ctftime()[str(self.ui.event_id.value())]
            self.ui.text_result.setText(json.dumps(result, indent=4))
            self.ui.statusBar.clearMessage()
        except (KeyError, json.decoder.JSONDecodeError):
            self.ui.text_result.clear()
            self.ui.text_result.setText('Results are not ready')

    def rating_formula(self) -> int:
        team_points = self.ui.team_points.value()
        best_points = self.ui.best_team_points.value()
        team_place = self.ui.team_place.value()
        weight = self.ui.weight.value()
        total_teams = self.ui.teams.value()
        rh_team_id = 186788
        place_k = 1 / team_place
        points_k = team_points / best_points
        result = (points_k + place_k) * weight / 1 / 1 + (team_place / total_teams)

        self.ui.rating_spinbox.setValue(result)
        best_rating = (1 + 1) * weight / 1 / 1 + (1 / total_teams)
        return best_rating

    def rating_spinbox_to_progressbar(self):
        self.ui.rating_spinbox.valueChanged.connect(self.ui.rating_progress.setValue)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ctftime()
    window.show()

    sys.exit(app.exec())
