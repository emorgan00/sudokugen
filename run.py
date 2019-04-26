import os, app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.app.run(host='0.0.0.0', port=port)