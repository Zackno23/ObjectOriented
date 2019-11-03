# データ型宣言： Username
# 属性： 実際のユーザーネーム
# ; ルール
# 4文字以上20時以下
#:できること
# ユーザー名を大文字に変換する


class Username:
    def __init__(self, name):
        self.name = name
        if not (4 <= len(name) <= 20):
            raise ValueError("字数がおうてへんで")
        if not name.isalpha():
            raise ValueError("アルファベットしかダメやで")
        name.upper()

    def print_Upper_name(self):
        name = self.name.upper()
        print(name)

print()



hibiki = Username(name='ひびきくん')
chikara = Username(name="chikara")

hibiki.print_name()
chikara.print_name()