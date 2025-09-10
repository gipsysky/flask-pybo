from pybo import create_app

app = create_app()

if __name__ == "__main__":
    # 외부 접속 가능하게 실행
    app.run(host="0.0.0.0", port=5000, debug=True)
