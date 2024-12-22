from flask import Flask, request, jsonify

# إنشاء التطبيق
app = Flask(__name__)

# الصفحة الرئيسية
@app.route('/')
def home():
    return "مرحباً بك في السيرفر الخاص بي!"

# صفحة API تعرض بيانات JSON
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "message": "مرحباً!",
        "status": "success",
        "data": {"key1": "value1", "key2": "value2"}
    }
    return jsonify(data)

# صفحة لإرسال بيانات (POST)
@app.route('/api/send', methods=['POST'])
def send_data():
    try:
        content = request.json  # استلام البيانات بصيغة JSON
        return jsonify({"message": "تم استلام البيانات بنجاح", "received_data": content})
    except Exception as e:
        return jsonify({"error": "فشل في استلام البيانات", "details": str(e)})

# صفحة غير موجودة
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "الصفحة غير موجودة"}), 404

# تشغيل السيرفر
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

