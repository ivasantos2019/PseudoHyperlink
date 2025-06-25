from PyQt5.QtWidgets import QAction, QMessageBox
from PyQt5.QtGui import QIcon
from qgis.gui import QgsMapTool
from qgis.core import QgsProject, QgsRectangle
import webbrowser
from . import resources_rc



class PseudoHyperlink:
    def __init__(self, iface):
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.tool = None

    def initGui(self):
        self.action = QAction(QIcon(":/icon.png"), "Pseudo Hyperlink", self.iface.mainWindow())
        self.action.triggered.connect(self.activate_tool)
        self.iface.addPluginToMenu("&Pseudo Hyperlink", self.action)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removePluginMenu("&Pseudo Hyperlink", self.action)
        self.iface.removeToolBarIcon(self.action)

    def activate_tool(self):
        layer = self.iface.activeLayer()
        if not layer:
            QMessageBox.warning(None, "Erro", "Selecione uma camada vetorial ativa.")
            return

        self.tool = HyperlinkTool(self.canvas, layer)
        self.canvas.setMapTool(self.tool)


class HyperlinkTool(QgsMapTool):
    def __init__(self, canvas, layer):
        super().__init__(canvas)
        self.canvas = canvas
        self.layer = layer

    def canvasReleaseEvent(self, event):
        # Obtem o ponto clicado no mapa
        point = self.canvas.getCoordinateTransform().toMapCoordinates(event.pos().x(), event.pos().y())

        # Cria uma área de busca pequena em torno do clique
        search_rect = QgsRectangle(point.x() - 0.0001, point.y() - 0.0001,
                                   point.x() + 0.0001, point.y() + 0.0001)

        # Busca feições dentro da área
        self.layer.selectByRect(search_rect)
        features = self.layer.selectedFeatures()

        if not features:
            QMessageBox.information(None, "Nenhuma feição", "Nenhuma feição encontrada nesse ponto.")
            return

        feature = features[0]  # pega a primeira feição encontrada

        if "link" not in feature.fields().names():
            QMessageBox.warning(None, "Campo ausente", "A feição não possui o campo 'link'.")
            return

        url = feature["link"]

        if url.startswith("http"):
            webbrowser.open(url)
        elif url.endswith(".pdf"):
            webbrowser.open("file://" + url)
        else:
            QMessageBox.information(None, "Link", f"Link: {url}")

        self.layer.removeSelection()
