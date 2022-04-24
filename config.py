import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
#DB_FILE = os.path.join(BASEDIR, 'database.sqlite')

class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #DB_FILE = DB_FILE
    #SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_FILE}'


class Production(Config):
    DEBUG = False


class Development(Config):
    ENV = "development"
    DEBUG = True



class Historique:
    histParis = ''' Paris est une destination touristique dès les débuts de l’histoire du tourisme. Partie incontournable du Grand Tour européen dès le 18e siècle, la ville connaît une augmentation continue de ses fréquentations touristiques tout au long du 19e et 20e siècle. Les infrastructures touristiques se multiplient, se diversifient et se spécialisent, grâce à des grandes manifestations telles que les expositions internationales et universelles. Les grands travaux et les projets d’embellissement suscitent l’admiration et attirent un public international. L’ancienneté et l’enracinement du fait touristique dans la capitale font que le tourisme fait partie de l’ADN urbain de la ville et se conjugue avec toutes les autres expressions urbaines '''

    histLyon = ''' Ce lieu est habité depuis la Préhistoire, la première ville, nommée Lugdunum, date de la Rome antique. Sous l'Empire romain, Lyon devient une puissante cité, capitale de la Gaule romaine.
                Lyon est avant tout réputée pour sa gastronomie : elle porte le titre de « capitale mondiale de la gastronomie » depuis 1935 et compte 20 restaurants étoilés Michelin. '''

    histMarseille = '''L’histoire de Marseille est complexe, faite de pouvoir, de commerce. Avec la conquête de la ville par Jules César, la part belle est donnée à Arles. Les affaires deviennent florissantes de l’autre côté du Rhône mais Marseille prend sa revanche 10 siècles plus tard avec l’arrivée des Francs. En témoignent, les édifices d’art roman bâtis dans la cité phocéenne. Cependant, c’est au XIXème siècle que Marseille vit un second âge d’or en redevenant une place forte du commerce en Méditerranée. Depuis cette période, la ville a toujours connu une position favorable. L’ensoleillement exceptionnel de la ville n’y est probablement pas pour rien et son histoire n’est pas finie.
                    '''

    histBordeaux = '''Si aujourd’hui Bordeaux est classé parmi les plus belles villes de France et attire des millions de visiteurs chaque année, la ville a été marquée par une histoire très riche qui prend naissance à l’antiquité. Simple village de forgerons gaulois à la base, la ville de Bordeaux par son histoire va connaître un développement fulgurant avec une économie florissante basée sur le commerce du vin.'''

    histToulouse = '''La ville est habitée depuis la Préhistoire. Son territoire est occupé par une tribu celte, les Volques Tectosages, jusqu'à l'arrivée des Romains, qui y fondent Tolosa. Au Ve siècle, Toulouse devient la capitale du Royaume Wisigoth. Au Moyen  ge, la ville va rester longtemps indépendante, avant de rejoindre le domaine royal en 1271. À la Renaissance, Toulouse vit une période de grande prospérité.'''

    histNice = '''L’histoire de Nice se caractérise essentiellement par deux éléments. C'est tout d'abord une ville frontière, qui a fréquemment changé de souveraineté. Elle a été ainsi successivement ligure, grecque et romaine, avant de faire partie du Royaume ostrogoth d'Italie, puis de l'Empire romain d'Orient et du royaume d'Italie (Saint-Empire Romain), devenant ensuite génoise, provençale, savoyarde, piémontaise et enfin française1. C'est par ailleurs une ville dont le développement a été très rapide et dû essentiellement au tourisme. Ces deux particularités ont entraîné des conséquences importantes sur le plan social, politique, économique, culturel et urbanistique'''


    histSaintM = '''L'histoire de Saint-Malo remonte à l'antiquité celtique, où cette région correspond à l'ancien centre maritime du
    peuple gaulois des Ambibarii : « Ambibares », appelés « Abrincatuii » (Abrincates) par Ptolémée, peuple de
    l'Avranchin, fraction des Unelles du Cotentin, dont le domaine s'étendait jusqu'à la cité d'Aleth (actuel Saint-Servan).
    Sous l'influence des Romains, la ville de Corseul, dans les terres, se développe aux dépens de la cité d'Aleth. Aleth
    reste un port important et à la fin du IIIe siècle les Romains choisissent de le fortifier'''

    histChamonix = '''L'histoire du village de Chamonix s'est construite autour d'une part de sa situation géographique exceptionnelle et d'autre part de la domination qu'exerça durant plusieurs siècles la Maison de Savoie sur ce territoire. Cette section relate les périodes et les faits historiques les plus marquants de la commune'''

    histStrasbourg = '''Strasbourg est une ville du Nord-Est de la France, située sur la rive gauche du Rhin. Fondée par les Romains en 12 av. J.-C. est aujourd’hui une ville symbole de la réconciliation franco-allemande. Il s’agit d’une des trois capitales européennes et est également la deuxième ville de France en nombre de congrès internationaux.'''

    histLille = '''La légende dit de Lille qu'elle a été fondée en 640 par les géants Lydéric et Phinaert. Mais on trouve la première trace de Lille dans un écrit de 1066.
    Lille sera tour à tour flamande, bourguignonne, espagnole avant de devenir française en 1667 lors de la conquête de la ville par Louis XIV.
    Ses agrandissements successifs au cours des siècles en ont fait aujourd'hui la quatrième métropole de France.'''

users = [
    {'name':'Paris',
    'photo': 'images_templates/Paris.jpg',
    'Historique' : Historique.histParis ,
     },
    {'name':'Lyon',
    'photo': 'images_templates/Lyon.jpg',
     'Historique' : Historique.histLyon ,
     },
    {'name':'Marseille',
    'photo': 'images_templates/Marseille.jpg',
     'Historique' : Historique.histMarseille,
     },
    {'name':'Bordeaux',
     'photo': 'images_templates/Bordeaux.jpg',
     'Historique' : Historique.histBordeaux,
     },
    {'name': 'Toulouse',
    'photo': 'images_templates/Toulouse.jpg',
    'Historique' : Historique.histToulouse,
     },
    {'name':'Nice',
    'photo': 'images_templates/Nice.jpg',
     'Historique' : Historique.histNice,
     },
    {'name':'Saint Malo',
    'photo': 'images_templates/Saint Malo.jpg',
    'Historique' : Historique.histSaintM,
     },
    {'name':'Chamonix Mont Blanc',
    'photo': 'images_templates/Chamonix Mont Blanc.jpg',
    'Historique' : Historique.histChamonix,
     },
    {'name':'Strasbourg',
    'photo': 'images_templates/Strasbourg.jpg',
     'Historique' : Historique.histStrasbourg,
     },
     {'name':'Lille',
     'photo': 'images_templates/Lille.jpg',
     'Historique' : Historique.histLille,
      },
]

class WebDevException(Exception):
    pass


# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
