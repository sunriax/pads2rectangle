from pathlib import Path
import pcbnew, wx

__version__ = "1.0"

class PcbPads2RectanglePads(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Create rectangle pads"
        self.category = "Export"
        self.show_toolbar_button = True
        self.icon_file_name = (Path(__file__).parent / "images" / "change_icon_32x32.png").as_posix()
        self.description = "Change all pads of a PCB to rectangle pads"

    def Run(self):
        board = pcbnew.GetBoard()

        for mod in board.GetFootprints():
            for pad in mod.Pads():
                if pad.GetShape() == pcbnew.PAD_SHAPE_ROUNDRECT:
                    pad.SetShape(pcbnew.PAD_SHAPE_RECT)
                    
        filler = pcbnew.ZONE_FILLER(board)
        filler.Fill(board.Zones())

        pcbnew.Refresh()

        board.Save(board.GetFileName())

PcbPads2RectanglePads().register()