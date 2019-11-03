# データ型宣言： Username
# 属性： 実際のユーザーネーム
# ; ルール
# 4文字以上20時以下
#:できること
# ユーザー名を大文字に変換する


class Username:
    def __init__(self, name):
        self.name = name
        alphabet_ascii = list(range(65, 91)) + list(range(97, 123))

        if not (4 <= len(name) <= 20):
            raise ValueError("字数がおうてへんで")
        for i in name:
            if not ord(i) in alphabet_ascii:
                raise ValueError("アルファベットやないとあかんで")


        name.upper()

    def print_Upper_name(self):
        name = self.name.upper()
        print(name)

print()

def alphabet_check(name):
    alphabet_ascii = list(range(65,91)) + list(range(97,123))
    for i in alphabet_ascii:
        if ord(i) in alphabet_ascii:
            return False
    else:
        return True

hibiki = Username(name='hibikisan')

hibiki.print_Upper_name()
