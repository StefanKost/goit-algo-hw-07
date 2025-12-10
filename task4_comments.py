from typing import List


class Comment:
    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author
        self.replies: List[Comment] = []
        self.is_deleted = False

    def add_reply(self, reply: 'Comment') -> None:
        self.replies.append(reply)

    def remove_reply(self, message: str = "This comment has been deleted.") -> None:
        self.text = message
        self.author = "Deleted"
        self.is_deleted = True

    def display(self, depth: int = 0) -> None:
        indent = "    " * depth

        author_display = f"[{self.author}]" if self.is_deleted else self.author
        print(f"{indent}{author_display}: {self.text}")

        for reply in self.replies:
            reply.display(depth + 1)


if __name__ == "__main__":
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()
