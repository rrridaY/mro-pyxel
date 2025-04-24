# 最初に実行するシーン
from Scenes.TitleScene import TitleScene


# デバッグ用 #####################
# from constants import *
# from Scenes.GameScene import GameScene
from __testenv__.TestScene import TestScene

#################################


class SceneManager:
    # 最初に実行するシーン
    current_scene = TestScene()

    @staticmethod
    def change_scene(scene):
        SceneManager.current_scene = scene

    @staticmethod
    def update():
        SceneManager.current_scene.update()

    @staticmethod
    def draw():
        SceneManager.current_scene.draw()