# pylint: disable=C
"""
This file contains the file, tier, and service templates which may be modified as necessary.
"""
import yaml

file_template = yaml.load("""version: "1.0"
schemaVersion: v1
app_id: AppDemo
tiers:""")
tier_template = yaml.load("""
      name: ds2db
      expose: True
      replicas: 1
      containers:
        - name: postgresdb
          image: jkshah/postgres:9.4
          environment:
            - POSTGRES_USER: postgres
              POSTGRES_PASSWORD: secret
          ports:
              - containerPort: 5432
          resources:
            request:
              min-cpus: 0.05
              min-memory: 64M
          volumes:
            - containerVolume: "/var/lib/postgresql/data"
              min-size: 1G""")

volume_template = yaml.load("""
                  containerVolume: "/var/lib/postgresql/data"
                  min-size: 1G""")

service_template = yaml.load("""
     name: rmq
     type: remote
     endpoints:
       - addresses:
          - ip: 1.2.3.4
         ports: 
          - port: 5672
            targetPort: 5672
            name: msgbus
            protocol: TCP""")
      

def greeting():
    print "\n#################################################################################################\n"

    print r"                     ________       ___.   .__  __    "
    print r"_____  ______ ______ \_____  \______\_ |__ |__|/  |_  "
    print r"\__  \ \____ \\____ \ /   |   \_  __ \ __ \|  \   __\ "
    print r" / __ \|  |_> >  |_> >    |    \  | \/ \_\ \  ||  |   "
    print r"(____  /   __/|   __/\_______  /__|  |___  /__||__|   "
    print r"     \/|__|   |__|           \/          \/           "


    print "\nHi! Welcome to appOrbit.\n\nIf you have any previously built app templates (YAML or JSON) for Kubernetes, \nthey may be seamlessly converted to the appOrbit template using this converter. \nFor starters, you need to tell us whether your kubernetes app template is one single all-in-one yaml document, or a bunch of yaml files. "

    print "\n#################################################################################################\n"