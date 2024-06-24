import random 
import requests
from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MEDIA_URL'] = settings.MEDIA_URL
        return context

class HomePageView(TemplateView):
    template_name = "home.html"
    
    def get(self, request, *args, **kwargs):
        art_works = [
        'https://lh3.googleusercontent.com/oONr3anlQoXcwyO3SrrxkXZc5ORwZRLSny8NokDVXkYH9jcaF45ka2pv7xncvz-6hwfuWSRxTwcWAJAcIwyELHJDCg=s0', 
        'https://lh3.googleusercontent.com/vP2gG8d9dwGg1rO-yHeAcr4GkYWDPnpsclIR_9bY1TqX3EDcA3ZXhL0HVRldfQrj3ouQWkkd8PyTI5s2UY0hRmJeUi_w=s0', 
        'https://lh3.googleusercontent.com/5PghNudUkjgYeRl_m3E5FSWDoVPzTKJ41rmlDY6UIzeZm89_L1taHDKmzkQudsZuhvQSG4up-qXypH8CwCuZoemfH-g=s0', 
        'https://lh3.googleusercontent.com/oR_ghUZeAELjd7TQx9oj2gvg_cUm6OkZXTzM7hsIt1JUiMHigP4z8E89BrsomYl5LCqnVakXIocsNELFFJrBjjIUEOk=s0', 
        'https://lh5.ggpht.com/l7FDthKPopBnIWTr4I6L_FPRHB6nJG8fKmOO9PoFRdsh1ta_3PijMfDGeYY0GafAxKiIfgAtPojuIvwXMfb9oo1H7Uo=s0', 
        'https://lh3.googleusercontent.com/hDN8_JS4BbbksBXkxIDUldJvooejHBfQjgD3b_Jr73HjVOAs8thpnvCJA3WUtQFxlbjx-QB1-IyqhgEiM4dFLFk1Sg=s0', 
        'https://lh5.ggpht.com/TYef1Bq7KoxZ06PWKy13JiEE-uF-IUcgGOPZNGwL8eBMxiP6suxWqYLIw2gV7bcns5kZGzSxI_c1MVryvrqeYFrQ4m8=s0', 
        'https://lh5.ggpht.com/UM6_H-pt4gzZsHeXlzvtgQyeCzfBAcTmTDrFRchd0W2Mlb18E553lscN85zwpMmDGqbSC23xGNAJ5Zr2mnX1SSCzEn4=s0', 
        'https://lh3.googleusercontent.com/JFH1H42dK0WIfM8GaB_s533Le3OsEiyNenC45XuFXo2WfFdWiuA75Ahqf5bBNPsWccXAIHCc6rQ43FGnLYMIH7zdxw=s0', 
        'https://lh3.googleusercontent.com/JFH1H42dK0WIfM8GaB_s533Le3OsEiyNenC45XuFXo2WfFdWiuA75Ahqf5bBNPsWccXAIHCc6rQ43FGnLYMIH7zdxw=s0', 
        'https://lh3.googleusercontent.com/qjkiSAC89H2lvsgogjCe6WGLzMFNgdoCLHwRngvUX6BACTFTggkzIXE99tz9Em-hTf44MS9YeRsxCjDkW7tfC9lprw=s0', 
        'https://lh6.ggpht.com/BF0tfZSo-iFNw-8FZEpi25zlwphOBrKB4eE-tViUeSWWjpiZTYEz8GHEkjQTdNoUxKClRexpN9vaiKjvaj4RavWoasA=s0', 
        'https://lh5.ggpht.com/1__LwWGcAIVD-C2TyCyxyChoDXVMA305FlolbpvQAy-yFrjtge9SS6DlSFSOqF3bCQ5I4xkugOuimDO3HzaptdemTiFA=s0', 
        'https://lh6.ggpht.com/UiLjunGTOOczHyAq2C4vY3R4VkMhoiXuEe-u8837609JsLmY8SJECVEoWrfK2h1B9hGHVovqFEgq9xyJ-mU3D8wLLfQ=s0', 
        'https://lh4.ggpht.com/Z7-8upzsAr4Mu2wftrbdJJe127mLKVd7nwxaMcq1c3mdwPUI-zI3ob3ZzNFYuJud3HcUoRU-y2eJqvHujsSSXghSvPHP=s0', 
        'https://lh5.ggpht.com/l7FDthKPopBnIWTr4I6L_FPRHB6nJG8fKmOO9PoFRdsh1ta_3PijMfDGeYY0GafAxKiIfgAtPojuIvwXMfb9oo1H7Uo=s0', 
        'https://lh6.ggpht.com/2dki6PKet45iGRMRsY6bgZ-tLgOxOrUQyPlekCM9_QbHfJK6yvLJdcRnW8ZMZmHpyP5QRAtjgZg7Bqx2chWLBH4E5w=s0', 
        'https://lh3.ggpht.com/lgGdRTPtdFb_AK6ZV5p49TbaKhTaCprUMNVdYe6qWPfBj4irGKMraNeO_RZt9qBCmFwR7qO4a1AIbQyL_rvDYGE33g=s0', 
        'https://lh4.ggpht.com/WE8I8zsg1FY56vs-cQn6YU7bwisW4rJ7o8ZfrpPsU2xqLecsf2JMygoGCttatGU5Jn35A2QpWVw1e2IzSygfMT-ecuY=s0', 
        'https://lh5.ggpht.com/MHtJm_-5MAK7bq7hW5OdMi3Prtjdgs5vJTIjquQfKH2XZgAHM-cM9AE93lVN8l-XbLjwTEP3ZcQvguq1B6zdkzl1gO9x=s0', 
        'https://lh3.ggpht.com/3oF0m7SlWkHd1N5bI0nzoi3GTvF9z7CKfSCzq91ZOTMsOErpFnedMmpQyil5ICN6_-Hvtkjjz1simrp4uqndO2ZHhwg=s0', 
        'https://lh4.ggpht.com/NjSL-iKMn86sfn0ek430-vK-idwrau9EsXgAYZ_wZ0f-zggfz9e6LmxlurXujDja5iyuBaVuWFLAeN3q09nPPvQWaA=s0', 
        'https://lh3.googleusercontent.com/HC--xmqAeqSFS787bCPIV0t0AokbmnwqCFf1j1xDAhkKTwAOCL0z1ldnncBkkPfBv9QskVUpAM7bMuxmaxq8vsdCZw=s0', 
        'https://lh4.ggpht.com/xlD9XhzKQ1fIK2UgZOGtiteEH80ERPLEFAzOBAVt261E6BysDGH4jCxb4EmmhMSzpn-OBANEV6K3lAv-AYCN5G7y9Rw=s0'
        ]
        image_url = random.choice(art_works)

        return render(request, 'home.html', {'image_url': image_url})


