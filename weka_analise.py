# encoding=utf8
import sys, os
#reload(sys)
#sys.setdefaultencoding('utf8')

import weka.core.jvm as jvm
from weka.core.converters import Loader, TextDirectoryLoader 
from weka.classifiers import Classifier
from weka.classifiers import Evaluation
from weka.core.classes import Random

jvm.start(class_path=['/Applications/weka-3-8-1/weka.jar'])


def get_data_dir():
    """
    Returns the data directory.
    :return: the data directory
    :rtype: str
    """
    rootdir = os.path.dirname(__file__)
    libdir = "data"
    return libdir

def print_title(title):
    """
    Prints the title underlined.
    :param title: the title to print
    :type title: str
    """

    print("\n" + title)
    print("=" * len(title))

def print_info(info):
    """
    Prints the info.
    :param info: the info to print
    :type info: str
    """

    print("\n" + info)

# load CSV file
print_title("Loading CSV file")
loader = Loader(classname="weka.core.converters.CSVLoader") 
data = loader.load_file(get_data_dir() + os.sep + "final-data.csv")
data.class_is_last()


from weka.classifiers import Classifier
cls = Classifier(classname="weka.classifiers.trees.J48", options=["-C", "0.3"])
cls.build_classifier(data)

print(cls.options)

print(cls)

import weka.plot.graph as graph   
graph.plot_dot_graph(cls.graph)


