import pyxel


# クラスのインポート(シーン)
from Scenes.BaseScene import BaseScene
# from Scenes.GameScene import GameScene

# クラスのインポート(データ処理)
from Classes.Vector2 import Vector2
from Classes.Button import Button
from Classes.Texture import Texture

# 関数のインポート


# 定数
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE, GAME_URL



# シェア用ボタン



class TitleScene(BaseScene):
    def __init__(self,max_score=0):
        super().__init__() # baseSceneのinitを呼び出す
        self.max_score = max_score



        

    def update(self):
        super().update()
        if pyxel.btnp(pyxel.KEY_SPACE):  # スペースキーでゲーム開始
            self.start_game(self.max_score)
        # マウス左クリック時
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            # マウスのクリック位置を取得
            clicked_pos = Vector2(pyxel.mouse_x, pyxel.mouse_y)

        

    def draw(self):
        pyxel.mouse(True)
        pyxel.cls(1)


        pyxel.text(60,20, GAME_TITLE, pyxel.COLOR_WHITE)
        
    def start_game(self,max_score=0):
        pass
        # from SceneManager import SceneManager
        # SceneManager.change_scene()# ここに次のシーンを入れる
