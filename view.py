import tkinter as Tk

from model import Model
from views.fig_canvas import Boxplot
from views.model_selection import Model_selection
from views.data_box import Data_box
from views.results import Results
from views.select_features import Select_features
from views.select_kernel import Select_kernel

class View:
  """
  Class for view object, contains or calls or GUI elements of the system
  """

  def __init__(self, root, controller):
    """
    Initialiser for View object, Sets root and controller object to be used for the view.
    Packs the master frame into the root given.

    Calls view objects that should be visible from launch 
    """
    self.frame = Tk.Frame(root)
    self.controller = controller
    
    self.frame.pack()
    self.model_selection = Model_selection(self.frame)
    self.data_box = Data_box(self.frame)
    self.results = Results(self.frame)
    self.select_kernel = Select_kernel(self.frame)

  def draw_boxplot(self, algorithms, results):
    """
    Draws boxplot view
    """
    self.boxplot = Boxplot(self.frame, algorithms, results)

  def draw_features(self, features):
    """
    draws feature selection view
    """
    self.select_features = Select_features(self.frame, features)


