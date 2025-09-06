from PyQt5 import QtCore, QtWidgets
import pandas as pd

class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, dataframe=pd.DataFrame(), parent=None):
        super().__init__(parent)
        self._dataframe = dataframe

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._dataframe)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self._dataframe.columns)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole and index.isValid():
            return str(self._dataframe.iat[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._dataframe.columns[section]
            else:
                return self._dataframe.index[section]
        return None
