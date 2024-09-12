FROM nginx:latest

# Instalar dependencias
RUN apt-get update && apt-get install -y iproute2 net-tools

# Copiar configuración de Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Establecer comando por defecto
CMD ["nginx", "-g", "daemon off;"]
