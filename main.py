from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

class ManouSocialApp(App):
    def build(self):
        # Layout الرئيسي للتطبيق
        root_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # عنوان التطبيق في الفوق
        title_label = Label(
            text='[b]Manou Social[/b]',
            markup=True,
            font_size=24,
            size_hint_y=None,
            height=50
        )
        root_layout.add_widget(title_label)

        # صندوق كتابة منشور جديد
        self.post_input = TextInput(
            text='',
            hint_text='ما الذي يدور في ذهنك؟...',
            size_hint_y=None,
            height=80,
            multiline=True
        )
        root_layout.add_widget(self.post_input)

        # زر النشر
        post_btn = Button(
            text='نشر (Post)',
            size_hint_y=None,
            height=50,
            background_color=(0.1, 0.5, 0.8, 1)
        )
        post_btn.bind(on_press=self.on_post_click)
        root_layout.add_widget(post_btn)

        # مكان عرض المنشورات (Feed)
        self.feed_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        self.feed_layout.bind(minimum_height=self.feed_layout.setter('height'))

        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(self.feed_layout)
        root_layout.add_widget(scroll_view)

        return root_layout

    def on_post_click(self, instance):
        post_text = self.post_input.text.strip()
        if post_text:
            # إضافة المنشور الجديد في قمة الـ Feed
            post_label = Label(
                text=post_text,
                size_hint_y=None,
                height=40,
                color=(1, 1, 1, 1)
            )
            self.feed_layout.add_widget(post_label)
            # تفريغ خانة الكتابة بعد النشر
            self.post_input.text = ''

if __name__ == '__main__':
    ManouSocialApp().run()

