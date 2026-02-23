from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

NEWS_API_KEY = "your_newsapi_key_here"  # Get free at newsapi.org
