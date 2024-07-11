from PIL import Image, ImageDraw, ImageFont

# image=Image.new('RGB', (640, 1100), 'white')
# draw=ImageDraw.Draw(image)

lisu6=ImageFont.truetype('SIMLI.TTF', 6*4.5)
stzhongsong18=ImageFont.truetype('STZHONGS.TTF', 18*4.5)
stzhongsong8=ImageFont.truetype('STZHONGS.TTF', 8*4.5)
simhei8=ImageFont.truetype('simhei.ttf', 8*4.5)
lisu8=ImageFont.truetype('SIMLI.TTF', 8*4.5)
stsong8=ImageFont.truetype('STSONG.TTF', 8*4.5)
stxihei6=ImageFont.truetype('STXIHEI.TTF', 6*4.5)

def draw_gua(gua: str):
    for i in range(len(gua)):
        draw.rectangle([170, 90+50*i, 640/2-10, 90+50*i+30], fill='black')
        draw.rectangle([640/2+10, 90+50*i, 640-170, 90+50*i+30], fill='black')
        c=gua[i]
        if c=='1':
            draw.rectangle([300, 90+50*i, 340, 90+50*i+30], fill='black')

def guaxiang(xiang: str):
    lines=xiang.split('\n')
    for i in range(len(lines)):
        draw.text([320+16, 645+8*4.5*1.1*i], lines[i], fill='black', font=stsong8, anchor='mt')

def guaci(ci: str):
    text='■'+ci
    length=len(text)
    lines=['■']
    for i in range(1, length):
        c=text[i]
        lines[-1]+=c
        if (i+1)%19==0:
            lines.append('')
    for i in range(len(lines)):
        draw.text([(640-19*6*4.5)/2, 840+6*4.5*1.1*i], lines[i], fill='black', font=stxihei6, anchor='lt')

gua=[
    '',
    '111111', #1
    '000000',
    '010001',
    '100010',
    '010111',
    '111010',
    '000010',
    '010000',
    '110111',
    '111011',
    '000111',
    '111000',
    '111101',
    '101111',
    '000100',
    '001000',
    '011001',
    '100110',
    '000011',
    '110000',
    '101001',
    '100101',
    '100000',
    '000001',
    '111001',
    '100111',
    '100001',
    '011110',
    '010010',
    '101101',
    '011100',
    '001110',
    '111100',
    '001111',
    '101000',
    '000101',
    '110101',
    '101011',
    '010100',
    '001010',
    '100011',
    '110001',
    '011111',
    '111110',
    '011000',
    '000110',
    '011010',
    '010110',
    '011101',
    '101110',
    '001001',
    '100100',
    '110100',
    '001011',
    '001101',
    '101100',
    '110110',
    '011011',
    '110010',
    '010011',
    '110011',
    '001100',
    '010101',
    '101010'
]

def draw_card(seq, name, rank, word, xiang, ci):
    # i=int(seq[1])
    draw_gua(gua[seq])
    
    draw.text([320, 425], f'第{seq}卦', fill='black', font=lisu6, anchor='mm')
    draw.text([320, 495], name, fill='black', font=stzhongsong18, anchor='mm')
    draw.text([320, 570], word, fill='black', font=simhei8, anchor='mm')

    rankx, ranky=520, 500
    draw.rounded_rectangle([rankx-25, ranky-45, rankx+25, ranky+45], 6, fill='lightgray')
    draw.text([rankx, ranky], rank[0]+'\n'+rank[1], fill='white', font=stzhongsong8, anchor='mm')

    draw.text([70, 650], '象曰：', fill='black', font=lisu8, anchor='lt')
    guaxiang(xiang)
    guaci(ci)

# draw_card(
#     '第1卦',
#     '乾为天',
#     '上上卦',
#     '自强不息',
#     '困龙得水好运交，\n不由喜气上眉梢，\n一切谋望皆如意，\n向后时运渐渐高。',
#     '象征天，喻龙（德才的君子），又象征纯粹的阳和健，表明兴盛强健。乾卦是根据万物变通的道理，以“元、亨、利、贞”为卦辞，示吉祥如意，教导人遵守天道的德行。'
# )

import json

with open('64.json', encoding='utf-8') as f:
    gua_json=json.loads(f.read())
for i in range(1, len(gua_json)):
    line=gua_json[i]
    segs=line.split()
    # print(segs)

    seq=i
    name=segs[1].split('·')[0]
    word, rank=segs[1].split('·')[1].split('【')
    xiang='\n'.join(segs[3:7])
    ci=segs[7]

    image=Image.new('RGB', [640, 1100], 'white')
    draw=ImageDraw.Draw(image)
    draw_card(seq, name, rank, word, xiang, ci)

    print(f'{i} ', end='')
    image.save(f'image2/{i}.jpg')

# image.show()
