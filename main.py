from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample videos data
videos_data = {
    "videos": [
        {
            "title": "Introduction to Machine Learning",
            "video_link": "https://videos.pexels.com/video-files/5377684/5377684-uhd_3840_2160_25fps.mp4",
            "view_status": "most viewed"
        },
        {
            "title": "Linear Regression Explained",
            "video_link": "https://videocdn.cdnpk.net/cdn/content/video/free/video0538/large_preview/_import_6305baed780c78.45222891.mp4?filename=1475087_people_business_3840x2160.mp4",
            "view_status": "less viewed"
        },
        {
            "title": "Python Basics for Data Science",
            "video_link": "https://videocdn.cdnpk.net/cdn/content/video/free/video0541/large_preview/_import_631844feed3b73.71891493.mp4?filename=1477064_people_business_3840x2160.mp4",
            "view_status": "less viewed"
        },
        {
            "title": "Deep Learning Fundamentals",
            "video_link": "https://v7.cdnpk.net/videvo_files/video/partners1382/large_preview/haaff4a57_A005_C008_1025RQ_V1-0251.mp4",
            "view_status": "most viewed"
        },
        {
            "title": "Introduction to Neural Networks",
            "video_link": "https://v4.cdnpk.net/videvo_files/video/free/video0464/large_preview/_import_6114c97a945b55.45070928.mp4",
            "view_status": "most viewed"
        },
        {
            "title": "Data Visualization Techniques",
            "video_link": "https://cdn.pixabay.com/video/2015/08/08/90-135735293_large.mp4",
            "view_status": "most viewed"
        }
    ]
}

@app.route('/')
def get_videos_data():
    return jsonify(videos_data)

if __name__ == '__main__':
    app.run(debug=True)
