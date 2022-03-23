from tkinter import *
from PIL import Image,ImageTk
import sqlite3
from sqlite3 import Error
from tkinter import messagebox
import matplotlib.pyplot as plt
conn = sqlite3.connect("main.db")#main database conn.
cursor=conn.cursor()