from pathlib import Path
import os
import sys

# ====================== sys.path 추가 ======================
BASE_DIR : str = os.path.dirname(Path(__file__).resolve().parent)
sys.path.append(BASE_DIR)
from cogs.real_time_search_word import RealTimeSearchWord
from cogs.lunch import Lunch
from cogs.homework import HomeWorkLunch,HomeWorkCSV
from cogs.quiz import CSV,Quiz
from cogs.image_crawling import GetImage
from cogs.page_views import GetPageViews
from cogs.file_upload import FileUpload
from main import Discord
# ======================               ======================