FROM mysql:8.0.21

# RUN useradd --user-group --system --create-home --no-log-init ahmed
# USER ahmed

WORKDIR /
COPY flask_final.sql .
# RUN  service mysql restart

# RUN mysql_upgrade --verbose
# RUN  mysql -u root flask < flask_final.sql