import mssql_functions as sql
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/recibosRecolector/<int:id_recolector>', methods=['GET'])
def recibos_recolector(id_recolector):
    recibos = sql.obtener_recibos_pendientes(id_recolector)
    return jsonify(recibos), 200


@app.route('/recibosEstatusRecolector/<int:id_recolector>/<string:estatus>', methods=['GET'])
def recibos_estatus_recolector(id_recolector, estatus):
    recibos = sql.obtener_recibos_por_estatus(id_recolector, estatus)
    return jsonify(recibos), 200


@app.route('/actualizarRecibo/<int:id_bitacora>', methods=['PUT'])
def actualizar_recibo(id_bitacora):
    data = request.get_json()

    id_recolector = data['id_recolector']
    fecha_pago = data['fecha_cobro']
    estatus = data['estatus']
    fecha_reprogramacion = data['fecha_reprogramacion']
    usuario_cancelacion = data['usuario_cancelacion']
    comentarios = data['comentarios']

    if sql.actualizar_recibo(id_bitacora, id_recolector, fecha_pago, estatus,
                          fecha_reprogramacion, usuario_cancelacion, comentarios):
        return jsonify({'message': 'Recibo actualizado'}), 200
    else:
        return jsonify({'error': 'Error al actualizar recibo'}), 500


@app.route('/recolectores')
def obtener_recolectores():
    recolectores = sql.obtener_recolectores()
    return jsonify(recolectores), 200


if __name__ == '__main__':
    app.run(debug=True, port=8082, host='0.0.0.0')
