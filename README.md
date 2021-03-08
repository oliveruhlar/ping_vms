#EntGuard release tests

This is the deploy and tests for GUI of EntGuard

##RUN
    1. In Config.ini set SSH variables where you want to release and run TESTs
    2. In Config.ini set paths to requiered files
    3. Run robot ./deploy_entguard.robot

##Config parser

The parser is just to parse variables set in COnfig.ini to deploy_entguard.robot

##Robot Framework

    1. Connects to ssh with public_key and username
    2. Deploys EG-O
    3. Deploys EG-S
    4. Run cypress tests for EG GUI
