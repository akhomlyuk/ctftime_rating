import json
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow
from functions import results_from_ctftime, event_information, rht_info, rht_best_res


class Ctftime(QMainWindow):
    def __init__(self):
        super(Ctftime, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.results_to_textedit()
        self.event_info_to_text_edit()
        self.rht_info_to_text_edit()
        self.rating_formula()
        self.rating_spinbox_to_progressbar()
        self.ui.rating_progress.setValue(self.ui.rating_spinbox.value())
        self.ui.best_team_points.valueChanged.connect(self.rating_formula)
        self.ui.event_id.editingFinished.connect(self.event_info_to_text_edit)
        self.ui.event_id.editingFinished.connect(self.results_to_textedit)
        self.ui.team_points.valueChanged.connect(self.rating_formula)
        self.ui.best_team_points.valueChanged.connect(self.rating_formula)
        self.ui.team_place.valueChanged.connect(self.rating_formula)
        self.ui.teams.valueChanged.connect(self.rating_formula)
        self.ui.weight.valueChanged.connect(self.rating_formula)

    def rht_info_to_text_edit(self):
        self.ui.rht_info.clear()
        try:
            rht = rht_info()
            rht_best = rht_best_res()
            # self.ui.rht_info.append('<a href="https://ctftime.org/team/186788">RedHazzarTeam</a>')
            self.ui.rht_info.append(f'🌍 Worldwide position: {rht["rating"]["2024"]["rating_place"]}')
            self.ui.rht_info.append(f'📈 RU position: {rht["rating"]["2024"]["country_place"]}')
            self.ui.rht_info.append(f'🎯 Rating points: {rht["rating"]["2024"]["rating_points"]}\n')
            self.ui.rht_info.append(f'ID: {rht["id"]}')
            self.ui.rht_info.append(f'Aliases: {rht["aliases"]}')
            nl = '\n'
            self.ui.rht_info.append(f'Best 10 results: {nl}')
            for i in rht_best[0]:
                for j in i:
                    if i[j].get("Place") == 3:
                        self.ui.rht_info.append(f'🥉 {j} * {i[j].get("Rating")}')
                    elif i[j].get("Place") == 2:
                        self.ui.rht_info.append(f'🥈 {j} * {i[j].get("Rating")}')
                    elif i[j].get("Place") == 1:
                        self.ui.rht_info.append(f'🥇 {j} * {i[j].get("Rating")}')
                    else:
                        self.ui.rht_info.append(f'▪️ {i[j].get("Place")} {j} * {i[j].get("Rating")}')
        except (KeyError, json.decoder.JSONDecodeError):
            self.ui.rht_info.clear()

    def event_info_to_text_edit(self):
        self.ui.event_info_text.clear()
        try:
            event_info = event_information(self.ui.event_id.value())
            # event_info = json.dumps(event_info, indent=4)
            # self.ui.event_info_text.setText(event_info)
            self.ui.event_info_text.append(f'{event_info["title"]}')
            self.ui.event_info_text.append(f'Site: <a href="{event_info["url"]}">{event_info["url"]}</a>')
            self.ui.event_info_text.append(f'Weight: {event_info["weight"]}' + '\n')
            self.ui.event_info_text.append(event_info['description'] + '\n')
            self.ui.event_info_text.append(f'Ctftime: <a href="{event_info["ctftime_url"]}">{event_info["ctftime_url"]}</a>' + '\n')
        except (KeyError, json.decoder.JSONDecodeError):
            self.ui.event_info_text.clear()
            self.ui.event_info_text.setText('Information not available')

    def results_to_textedit(self):
        try:
            result = results_from_ctftime()[str(self.ui.event_id.value())]
            result = json.dumps(result, indent=4)
            self.ui.text_result.setText(result)
        except (KeyError, json.decoder.JSONDecodeError):
            self.ui.text_result.clear()
            self.ui.text_result.setText('Results are not ready')

    def rating_formula(self) -> int:
        team_points = self.ui.team_points.value()
        best_points = self.ui.best_team_points.value()
        team_place = self.ui.team_place.value()
        weight = self.ui.weight.value()
        total_teams = self.ui.teams.value()
        place_k = 1 / team_place
        points_k = team_points / best_points
        result = (points_k + place_k) * weight / 1 / 1 + (team_place / total_teams)
        best_rating = (1 + 1) * weight / 1 / 1 + (1 / total_teams)
        self.ui.rating_spinbox.setValue(result)
        self.ui.rating_progress.setMaximum(best_rating)
        return best_rating

    def rating_spinbox_to_progressbar(self):
        self.ui.rating_spinbox.valueChanged.connect(self.ui.rating_progress.setValue)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ctftime()
    window.show()
    sys.exit(app.exec())
