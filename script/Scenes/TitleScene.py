import pyxel


# クラスのインポート(シーン)
from Scenes.BaseScene import BaseScene
# from Scenes.GameScene import GameScene

# クラスのインポート(データ処理)
from Classes.Vector2 import Vector2
from Classes.Button import Button,TwitterShareButton
from Classes.Texture import Texture

# 関数のインポート


# 定数
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE, GAME_URL



# シェア用ボタン
Xbutton = Button(pos=Vector2(20, 80), texture=Texture(0, Vector2(0, 24), Vector2(16, 17),colkey=pyxel.COLOR_BLACK), event_func=TwitterShareButton.open_shareURL_with_score)



class TitleScene(BaseScene):
    def __init__(self,max_score=0):
        super().__init__() # baseSceneのinitを呼び出す
        self.max_score = max_score

        self.sharebutton = Xbutton# ボタン


        

    def update(self):
        super().update()
        if pyxel.btnp(pyxel.KEY_SPACE):  # スペースキーでゲーム開始
            self.start_game(self.max_score)
        # マウス左クリック時
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            # マウスのクリック位置を取得
            clicked_pos = Vector2(pyxel.mouse_x, pyxel.mouse_y)

            # シェア用ボタンがクリックされた場合
            if self.sharebutton.is_clicked(clicked_pos):
                print("Share button is clicked")
                self.sharebutton.click_event(score=self.max_score)
        

    def draw(self):
        pyxel.mouse(True)
        pyxel.cls(1)


        pyxel.text(60,20, GAME_TITLE, pyxel.COLOR_WHITE)
        self.sharebutton.draw()
        pyxel.text(self.sharebutton.pos.x + self.sharebutton.texture.size.x, 
                   self.sharebutton.pos.y + 5, 
                   f"<-Share\nYour Score: {self.max_score}",
                   pyxel.COLOR_WHITE
                   )
        
    def start_game(self,max_score=0):
        pass
        # from SceneManager import SceneManager
        # SceneManager.change_scene()# ここに次のシーンを入れる
