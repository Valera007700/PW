This scenario is boots with simulator connector#1 in Preparing state and is meant to be used for testing RemoteStart transaction

## Configuration

1. Set a URL for an environment you want to run the simulation at in `config.json`: 
```
  "supervisionURLs": [
    "wss://dm-dev.incharge.network:443/ocpp"
  ],
```

Use "wss://dm-dev.incharge.network:443/ocpp" for dev and "wss://dm-uat.incharge.network:443/ocpp" for UAT.

1. Set the identity of the charger you want to simulate at `remote-scenario/station-templates/abb_charger.json`:
```
  "baseName": "yars_created_sn_4",
```

1. Set RFID authorization tag for a charger in `remote-start-scenario/station-templates/abb_charger.json`. If you using NOA authorization (as we usually do with sumulator), skip this step, as it is preconfigured with "NOA".
```
[
  "YOUR-RFID-HERE"
]
```

1. Run the simulation as root README.md describes
