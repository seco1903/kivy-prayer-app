import requests
import datetime
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.button import Button
from kivy.uix.image import Image


class SecoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"

        screen = MDScreen()

        # Arka plan resmi
        bg_image = Image(
            source='cami.jpg',
            allow_stretch=True,
            keep_ratio=False
        )
        screen.add_widget(bg_image)

        # SOL KÖŞE: Tarih Göstergesi
        bugun = datetime.date.today().strftime("%d.%m.%Y")
        self.tarih_btn = Button(
            text=f"Tarih:\n{bugun}",
            font_size="12sp",
            bold=True,
            halign="center",
            valign="middle",
            padding=[10, 5],
            size_hint=(None, None),
            pos_hint={'x': 0.03, 'top': 0.95},
            background_color=(0.1, 0.4, 0.4, 0.85)
        )
        self.tarih_btn.bind(texture_size=self.tarih_btn.setter('size'))
        screen.add_widget(self.tarih_btn)

        # SAĞ KÖŞE: Canlı Dijital Saat Göstergesi
        self.saat_btn = Button(
            text="Saat:\n00:00:00",
            font_size="12sp",
            bold=True,
            halign="center",
            valign="middle",
            padding=[10, 5],
            size_hint=(None, None),
            pos_hint={'right': 0.97, 'top': 0.95},
            background_color=(0.1, 0.4, 0.4, 0.85)
        )
        self.saat_btn.bind(texture_size=self.saat_btn.setter('size'))
        screen.add_widget(self.saat_btn)

        # Her saniye saati güncellemek için zamanlayıcı
        Clock.schedule_interval(self.saati_guncelle, 1)

        # Başlık Kutusu
        self.title_btn = Button(
            text="Seco App - Namaz Vakitleri",
            font_size="16sp",
            bold=True,
            halign="center",
            valign="middle",
            padding=[20, 10],
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'top': 0.90},
            background_color=(0.1, 0.4, 0.4, 0.85)
        )
        self.title_btn.bind(texture_size=self.title_btn.setter('size'))
        screen.add_widget(self.title_btn)

        # SOL MİNARE ÜSTÜ: KİRAZ Kutusu
        self.kiraz_btn = Button(
            text="KİRAZ\n\nVakitleri görmek için butona basın.",
            font_size="13sp",
            bold=True,
            halign="center",
            valign="middle",
            size_hint=(None, None),
            width=220,
            height=130,
            pos_hint={'center_x': 0.22, 'center_y': 0.55},
            background_color=(0.1, 0.3, 0.3, 0.85)
        )
        self.kiraz_btn.bind(texture_size=self.kiraz_btn.setter('size'))
        screen.add_widget(self.kiraz_btn)

        # SAĞ MİNARE ÜSTÜ: ÖDEMİŞ Kutusu
        self.odemis_btn = Button(
            text="ÖDEMİŞ\n\nVakitleri görmek için butona basın.",
            font_size="13sp",
            bold=True,
            halign="center",
            valign="middle",
            size_hint=(None, None),
            width=220,
            height=130,
            pos_hint={'center_x': 0.78, 'center_y': 0.55},
            background_color=(0.1, 0.3, 0.3, 0.85)
        )
        self.odemis_btn.bind(texture_size=self.odemis_btn.setter('size'))
        screen.add_widget(self.odemis_btn)

        # ORTA AŞAĞI: Günlük Hadis Kutusu
        self.hadis_btn = Button(
            text="\"Ameller niyetlere göredir.\" (Buhârî)",
            font_size="13sp",
            bold=True,
            halign="center",
            valign="middle",
            padding=[15, 10],
            size_hint=(None, None),
            width=420,
            height=70,
            pos_hint={'center_x': 0.5, 'y': 0.22},
            background_color=(0.1, 0.35, 0.35, 0.85)
        )
        self.hadis_btn.bind(texture_size=self.hadis_btn.setter('size'))
        screen.add_widget(self.hadis_btn)

        # Vakitleri Çek Butonu (En alt)
        btn = Button(
            text="Vakitleri Çek",
            font_size="15sp",
            bold=True,
            size_hint=(None, None),
            width=180,
            height=45,
            pos_hint={'center_x': 0.5, 'y': 0.08},
            background_color=(0.1, 0.6, 0.6, 1),
            on_release=self.vakitleri_getir
        )
        screen.add_widget(btn)

        return screen

    def saati_guncelle(self, dt):
        simdiki_zaman = datetime.datetime.now().strftime("%H:%M:%S")
        self.saat_btn.text = f"Saat:\n{simdiki_zaman}"

    def vakitleri_getir(self, instance):
        try:
            url_kiraz = "https://api.aladhan.com/v1/timingsByCity?city=Kiraz&country=Turkey&method=13"
            response_kiraz = requests.get(url_kiraz, timeout=5)

            url_odemis = "https://api.aladhan.com/v1/timingsByCity?city=Odemis&country=Turkey&method=13"
            response_odemis = requests.get(url_odemis, timeout=5)

            if response_kiraz.status_code == 200 and response_odemis.status_code == 200:
                k_data = response_kiraz.json()['data']['timings']
                k_metin = (
                    "KİRAZ\n"
                    f"İmsak: {k_data.get('Fajr')} | Öğle: {k_data.get('Dhuhr')}\n"
                    f"İkindi: {k_data.get('Asr')} | Akşam: {k_data.get('Maghrib')}\n"
                    f"Yatsı: {k_data.get('Isha')}"
                )
                self.kiraz_btn.text = k_metin

                o_data = response_odemis.json()['data']['timings']
                o_metin = (
                    "ÖDEMİŞ\n"
                    f"İmsak: {o_data.get('Fajr')} | Öğle: {o_data.get('Dhuhr')}\n"
                    f"İkindi: {o_data.get('Asr')} | Akşam: {o_data.get('Maghrib')}\n"
                    f"Yatsı: {o_data.get('Isha')}"
                )
                self.odemis_btn.text = o_metin
            else:
                self.kiraz_btn.text = "KİRAZ\nHata oluştu."
                self.odemis_btn.text = "ÖDEMİŞ\nHata oluştu."

        except Exception as e:
            self.kiraz_btn.text = "KİRAZ\nBağlantı hatası."
            self.odemis_btn.text = "ÖDEMİŞ\nBağlantı hatası."


if __name__ == '__main__':
    SecoApp().run()