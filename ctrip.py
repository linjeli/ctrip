import json
import requests

def post():
    resp = requests.post(url, data=json.dumps(data)).json()
    print(resp)
    items = resp.get('result').get('items')
    print(len(items))
    for item in items:
        images = item.get('images')
        if images:
            for img in images:
                imageSrcUrl = img.get('imageSrcUrl')
                img_urls.append(imageSrcUrl)
                print(imageSrcUrl)

def saveImg(img_urls):
    '''保存图'''
    i = 1
    for url in img_urls:
        img = requests.get(url)
        with open('./ctrip/' + str(i) +'.jpg', 'wb') as f:
            f.write(img.content)
            print(f'正在保存{i}')
            i += 1

if __name__ == '__main__':
    img_urls = []
    url = 'https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'cookie': 'ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; _RSG=.xq8YdHCakAOelmkVQNkX8; _RDG=28c4e484cc16e624db1812bd10f725343f; _RGUID=aba43119-e223-4efe-886e-5da7eec2fa18; _ga=GA1.2.1458938416.1642496022; _gid=GA1.2.778584023.1642496022; MKT_CKID=1642496021878.63lzz.9p80; MKT_Pagesource=PC; _bfaStatusPVSend=1; GUID=09031089212143492169; nfes_isSupportWebP=1; _gcl_au=1.1.1887433388.1642556619; MKT_OrderClick=ASID=4897799747&AID=4897&CSID=799747&OUID=xiecheng508&CT=1642556622358&CURL=https%3A%2F%2Fhotels.ctrip.com%2F%3Fallianceid%3D4897%26sid%3D799747%26ouid%3Dxiecheng508%26bd_vid%3D8279219761831173060%26keywordid%3D138219528443&VAL={"pc_vid":"1642496019085.2t7xks"}; appFloatCnt=1; StartCity_Pkg=PkgStartCity=2; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&createtime=1642556680&Expires=1643161480045; _bfi=p1%3D290510%26p2%3D290510%26v1%3D10%26v2%3D9; MKT_CKID_LMT=1642584535847; __zpspc=9.5.1642584535.1642584535.1%232%7Cwww.baidu.com%7C%7C%7C%7C%23; _RF1=113.108.77.66; _jzqco=%7C%7C%7C%7C1642584537097%7C1.965214197.1642496021929.1642574556347.1642584535837.1642574556347.1642584535837.0.0.0.9.9; _bfa=1.1642496019085.2t7xks.1.1642574551407.1642584530190.4.12; _bfs=1.3; _bfaStatus=send',
        'cookieorigin': 'https://you.ctrip.com',
        'origin': 'https://you.ctrip.com',
        'referer': 'https://you.ctrip.com/',
        'content-type': 'application/json',
    }
    for page in range(40):
        print('图片列表数：', len(img_urls))
        data = {
            'arg': {
              "channelType": 2,
              "collapseType": 0,
              "commentTagId": 0,
              "pageIndex": page + 1,
              "pageSize": 10,
              "poiId": 97470,
              "sourceType": 1,
              "sortType": 3,
              "starType": 0
            },
            'head': {
              "cid": "09031089212143492169",
              "ctok": "",
              "cver": "1.0",
              "lang": "01",
              "sid": "8888",
              "syscode": "09",
              "auth": "",
              "xsid": "",
              "extension": []
            }
        }
        # params =
        #     '_fxpcqlniredt': '09031089212143492169',
        #     'x-traceID': '09031089212143492169-1642585510010-1512200',
        # }
        post()
    saveImg(img_urls)