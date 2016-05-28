import sys
from workflow import Workflow, ICON_WEB, web

def main(wf):
    hat = ""

    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    url = 'http://www.iett.gov.tr/tr/main/ajaxHatSonuc/?q='+query+'&format=json'
    r = web.get(url)
    r.raise_for_status()
    result = r.json()

    hatlar = result['item']['yon_1']['kalkis_saati']
    bilgi = result['item']['hat_no'] + " " + result['item']['yon_1']['durak_adi']


    for hat in hatlar:
        wf.add_item(title=hat['saat']['zaman'], subtitle=bilgi)
    
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))