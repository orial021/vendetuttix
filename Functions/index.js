const functions = require('firebase-functions');
const express = require('express');
const { createServer } = require('http');
const { default: fastify } = require('fastify');

const app = fastify();

// Ruta principal para todas las solicitudes de tu backend
app.all('**', async (request, reply) => {
  try {
    // Lógica de backend común para todas las rutas
    const endpoint = request.url.replace('/', ''); // Extrae el endpoint
    let data;

    switch (endpoint) {
      case 'mi-endpoint-1':
        // Lógica específica para /api/mi-endpoint-1
        data = { message: 'Respuesta desde mi-endpoint-1' };
        break;
      case 'mi-endpoint-2':
        // Lógica específica para /api/mi-endpoint-2
        data = { message: 'Respuesta desde mi-endpoint-2' };
        break;
      // Agrega más casos según tus rutas
      default:
        reply.status(404).send({ error: 'Ruta no encontrada' });
        return;
    }

    reply.send(data);
  } catch (error) {
    reply.status(500).send({ error: 'Error en el servidor' });
  }
});

const server = createServer(app);

exports.myBackendFunction = functions.https.onRequest(server);
