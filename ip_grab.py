from datetime import date, datetime
import os, re, sys, argparse, urllib.parse, logging, requests

parser = argparse.ArgumentParser(
description="This script will extract domains from the file you specify and add it to a final file"
)
parser.add_argument('--file', action="store", default=None, dest='inputFile',
    help="Specify the file to extract domains from")
parser.add_argument('--url', action="store", default=None, dest='url',
    help="Specify the web page to extract domains from. One at a time for now")
parser.add_argument('--target', action="store", default='all', dest='target',
    help="Specify the target top-level domain you'd like to find and extract e.g. uber.com")
parser.add_argument('--verbose', action="store_true", default=False, dest='verbose',
    help="Enable slightly more verbose console output")
args = parser.parse_args()





outputFile = "combined.txt".format(args.target)

def extractDomains(args, inputFile, rawData):
    domains = []

    if not args.target:
        print("No target specified, defaulting to finding 'all' domains")

    for i in rawData:
        matches = re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,3}',i)
        if not args.target.lower() == 'all':
            for j in matches:

                if j.find(args.target.lower()) != -1:
                    domains.append(j)
        else:
            for j in matches:
                if j.find('') != -1:
                    domains.append(j)
                elif j.find('') != -1:
                    domains.append(j)

    return domains


results = []

# If files are specified, check them
if args.inputFile:
    fileList = args.inputFile.split(',')
    for inputFile in fileList:
        try:
            with open(inputFile, 'r') as f:
                rawData = f.read().splitlines()
        except UnicodeDecodeError:
            with open(inputFile, 'r', encoding="ISO-8859-1") as f:
                rawData = f.read().splitlines()

        results += extractDomains(args, inputFile, rawData)


# sort and dedupe our results
finalDomains = sorted(set(results))

# read all the domains we already have.
try:
    with open(outputFile, 'r') as out:
        oldDomains = out.read().splitlines()

# If no final file, create one
except FileNotFoundError:
    print("Output file not found. Creating one...")

    with open(outputFile, 'w') as out:
        for i in finalDomains:
            out.write("{}\n".format(i))

    print("Assets extracted")

# loop through fresh domains. If we don't already have it, add it to final file, notify us, log it.
newDomains = []
with open(outputFile, 'a') as out:
    for i in finalDomains:
            newDomains.append(i)
            out.write("{}\n".format(i))
    print("Assets extracted")

# filter domain names

fpointer = open("cleaned_from_duplicates.txt", "r");
print ("Start cleanup")

for i in fpointer.readlines():
   line= re.findall(r'2d|".abbott$|.abogado$|.ac$|.academy$|.accountant$|.accountants$|.active$|.actor$|.ad$|.ads$|.adult$|.ae$|.aero$|.af$|.afl$|.ag$|.agency$|.ai$|.airforce$|.al$|.allfinanz$|.alsace$|.am$|.amsterdam$|.an$|.android$|.ao$|.apartments$|.aq$|.aquarelle$|.ar$|.archi$|.army$|.arpa$|.as$|.asia$|.associates$|.at$|.attorney$|.au$|.auction$|.audio$|.autos$|.aw$|.ax$|.axa$|.az$|.ba$|.band$|.bank$|.bar$|.barclaycard$|.barclays$|.bargains$|.bauhaus$|.bayern$|.bb$|.bbc$|.bd$|.be$|.beer$|.berlin$|.best$|.bf$|.bg$|.bh$|.bi$|.bid$|.bike$|.bingo$|.bio$|.biz$|.bj$|.bl$|.black$|.blackfriday$|.bloomberg$|.blue$|.bm$|.bmw$|.bn$|.bnpparibas$|.bo$|.boats$|.bond$|.boo$|.boutique$|.bq$|.br$|.brussels$|.bs$|.bt$|.budapest$|.build$|.builders$|.business$|.buzz$|.bv$|.bw$|.by$|.bz$|.bzh$|.ca$|.cab$|.cafe$|.cal$|.camera$|.camp$|.cancerresearch$|.canon$|.capetown$|.capital$|.caravan$|.cards$|.care$|.career$|.careers$|.cartier$|.casa$|.cash$|.casino$|.cat$|.catering$|.cbn$|.cc$|.cd$|.center$|.ceo$|.cern$|.cf$|.cfd$|.cg$|.ch$|.channel$|.chat$|.cheap$|.chloe$|.christmas$|.chrome$|.church$|.ci$|.citic$|.city$|.ck$|.cl$|.claims$|.cleaning$|.click$|.clinic$|.clothing$|.club$|.cm$|.cn$|.co$|.coach$|.codes$|.coffee$|.college$|.cologne$|.com$|.community$|.company$|.computer$|.condos$|.construction$|.consulting$|.contractors$|.cooking$|.cool$|.coop$|.country$|.courses$|.cr$|.credit$|.creditcard$|.cricket$|.crs$|.cruises$|.cu$|.cuisinella$|.cv$|.cw$|.cx$|.cy$|.cymru$|.cyou$|.cz$|.dabur$|.dad$|.dance$|.date$|.dating$|.datsun$|.day$|.dclk$|.de$|.deals$|.degree$|.delivery$|.democrat$|.dental$|.dentist$|.desi$|.design$|.dev$|.diamonds$|.diet$|.digital$|.direct$|.directory$|.discount$|.dj$|.dk$|.dm$|.dnp$|.do$|.docs$|.doha$|.domains$|.doosan$|.download$|.durban$|.dvag$|.dz$|.eat$|.ec$|.edu$|.education$|.ee$|.eg$|.eh$|.email$|.emerck$|.energy$|.engineer$|.engineering$|.enterprises$|.epson$|.equipment$|.er$|.erni$|.es$|.esq$|.estate$|.et$|.eu$|.eurovision$|.eus$|.events$|.everbank$|.exchange$|.expert$|.exposed$|.express$|.fail$|.faith$|.fan$|.fans$|.farm$|.fashion$|.feedback$|.film$|.finance$|.financial$|.firmdale$|.fish$|.fishing$|.fit$|.fitness$|.fj$|.fk$|.flights$|.florist$|.flowers$|.flsmidth$|.fly$|.fm$|.fo$|.foo$|.football$|.forex$|.forsale$|.foundation$|.fr$|.frl$|.frogans$|.fund$|.furniture$|.futbol$|.ga$|.gal$|.gallery$|.garden$|.gb$|.gbiz$|.gd$|.gdn$|.ge$|.gent$|.gf$|.gg$|.ggee$|.gh$|.gi$|.gift$|.gifts$|.gives$|.gl$|.glass$|.gle$|.global$|.globo$|.gm$|.gmail$|.gmo$|.gmx$|.gn$|.gold$|.goldpoint$|.golf$|.goo$|.goog$|.google$|.gop$|.gov$|.gp$|.gq$|.gr$|.graphics$|.gratis$|.green$|.gripe$|.gs$|.gt$|.gu$|.guge$|.guide$|.guru$|.gw$|.gy$|.hamburg$|.hangout$|.haus$|.healthcare$|.help$|.here$|.hermes$|.hiphop$|.hiv$|.hk$|.hm$|.hn$|.holdings$|.holiday$|.homes$|.horse$|.host$|.hosting$|.house$|.how$|.hr$|.ht$|.hu$|.ibm$|.id$|.ie$|.ifm$|.il$|.im$|.immo$|.immobilien$|.in$|.industries$|.infiniti$|.info$|.ink$|.institute$|.insure$|.int$|.international$|.investments$|.io$|.iq$|.ir$|.irish$|.is$|.it$|.iwc$|.jcb$|.je$|.jetzt$|.jm$|.jo$|.jobs$|.joburg$|.jp$|.juegos$|.kaufen$|.kddi$|.ke$|.kg$|.kh$|.ki$|.kim$|.kitchen$|.kiwi$|.km$|.kn$|.koeln$|.komatsu$|.kp$|.kr$|.krd$|.kred$|.kw$|.ky$|.kyoto$|.kz$|.la$|.lacaixa$|.land$|.lat$|.latrobe$|.lawyer$|.lb$|.lc$|.lds$|.lease$|.leclerc$|.legal$|.lgbt$|.li$|.lidl$|.life$|.lighting$|.limited$|.limo$|.link$|.lk$|.loan$|.loans$|.london$|.lotte$|.lotto$|.love$|.lr$|.ls$|.lt$|.ltda$|.lu$|.luxe$|.luxury$|.lv$|.ly$|.ma$|.madrid$|.maif$|.maison$|.management$|.mango$|.market$|.marketing$|.markets$|.marriott$|.mc$|.md$|.me$|.media$|.meet$|.melbourne$|.meme$|.memorial$|.menu$|.mf$|.mg$|.mh$|.miami$|.mil$|.mini$|.mk$|.ml$|.mm$|.mma$|.mn$|.mo$|.mobi$|.moda$|.moe$|.monash$|.money$|.mormon$|.mortgage$|.moscow$|.motorcycles$|.mov$|.movie$|.mp$|.mq$|.mr$|.ms$|.mt$|.mtn$|.mtpc$|.mu$|.museum$|.mv$|.mw$|.mx$|.my$|.mz$|.na$|.nagoya$|.name$|.navy$|.nc$|.ne$|.net$|.network$|.new$|.news$|.nexus$|.nf$|.ng$|.ngo$|.nhk$|.ni$|.nl$|.no$|.np$|.nr$|.nra$|.nrw$|.ntt$|.nu$|.nyc$|.nz$|.okinawa$|.om$|.one$|.onl$|.online$|.ooo$|.org$|.organic$|.osaka$|.otsuka$|.ovh$|.pa$|.page$|.panerai$|.paris$|.partners$|.parts$|.party$|.pe$|.pf$|.pg$|.ph$|.pharmacy$|.photo$|.photography$|.photos$|.physio$|.piaget$|.pics$|.pictet$|.pictures$|.pink$|.pizza$|.pk$|.pl$|.place$|.plumbing$|.plus$|.pm$|.pohl$|.poker$|.porn$|.post$|.pr$|.praxi$|.press$|.pro$|.prod$|.productions$|.prof$|.properties$|.property$|.ps$|.pt$|.pub$|.pw$|.py$|.qa$|.qpon$|.quebec$|.racing$|.re$|.realtor$|.recipes$|.red$|.redstone$|.rehab$|.reise$|.reisen$|.reit$|.ren$|.rentals$|.repair$|.report$|.republican$|.rest$|.restaurant$|.review$|.reviews$|.rich$|.rio$|.rip$|.ro$|.rocks$|.rodeo$|.rs$|.rsvp$|.ru$|.ruhr$|.rw$|.ryukyu$|.sa$|.saarland$|.sale$|.samsung$|.sap$|.sarl$|.saxo$|.sb$|.sc$|.sca$|.scb$|.schmidt$|.scholarships$|.school$|.schule$|.schwarz$|.science$|.scot$|.sd$|.se$|.services$|.sew$|.sexy$|.sg$|.sh$|.shiksha$|.shoes$|.shriram$|.si$|.singles$|.site$|.sj$|.sk$|.sky$|.sl$|.sm$|.sn$|.so$|.social$|.software$|.sohu$|.solar$|.solutions$|.soy$|.space$|.spiegel$|.spreadbetting$|.sr$|.ss$|.st$|.study$|.style$|.su$|.sucks$|.supplies$|.supply$|.support$|.surf$|.surgery$|.suzuki$|.sv$|.sx$|.sy$|.sydney$|.systems$|.sz$|.taipei$|.tattoo$|.tax$|.tc$|.td$|.tech$|.technology$|.tel$|.temasek$|.tennis$|.tf$|.tg$|.th$|.tickets$|.tienda$|.tips$|.tires$|.tirol$|.tj$|.tk$|.tl$|.tm$|.tn$|.to$|.today$|.tokyo$|.tools$|.top$|.toshiba$|.tours$|.town$|.toys$|.tp$|.tr$|.trade$|.trading$|.training$|.travel$|.trust$|.tt$|.tui$|.tv$|.tw$|.tz$|.ua$|.ug$|.uk$|.um$|.university$|.uno$|.uol$|.us$|.uy$|.uz$|.va$|.vacations$|.vc$|.ve$|.vegas$|.ventures$|.versicherung$|.vet$|.vg$|.vi$|.viajes$|.video$|.villas$|.vision$|.vlaanderen$|.vn$|.vodka$|.vote$|.voting$|.voto$|.voyage$|.vu$|.wales$|.wang$|.watch$|.webcam$|.website$|.wed$|.wedding$|.wf$|.whoswho$|.wien$|.wiki$|.williamhill$|.win$|.wme$|.work$|.works$|.world$|.ws$|.wtc$|.wtf$|.xin$|.xxx$|.xyz$|.yachts$|.yandex$|.ye$|.yodobashi$|.yoga$|.yokohama$|.youtube$|.yt$|.za$|.zm$|.zone$|.zuerich$|.zw$', i);

   if line:
    #print(i);

    if line:

        file = open("text1.txt", "a")
        file.write(i)
        file.close()

# extract real domains only

#write to file function
def writerx (a):
    xfile = open("domains_alive.txt", "a")
    xfile.write("\n")
    xfile.write(str(a))
    xfile.write("\n")
    xfile.close()

liner = open("text1.txt", "r");

for a in liner.readlines():
    import socket
    #print(a)
    cleaned=a.strip()

#try to get hostname of domain
    try:
     addr1 = socket.gethostbyname_ex(cleaned)
     #print (addr1)
     #print (a)
     writerx(a)



    except:
        #print ("Bad domain")
        pass

liner.close()


f = open("combined.txt",'r')
text = f.read()
ips = []
regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',text)
if regex is not None:
    for match in regex:
        if match not in ips:
            ips.append(match)
           #print(match)
            writerx(match)



with open('text1.txt') as result:
    uniqlines = set(result.readlines())
    with open('cleanedfull.txt', 'w') as rmdup:
        rmdup.writelines(set(uniqlines))
        print ("Duplicates removed")