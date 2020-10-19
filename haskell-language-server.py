#!/usr/bin/env python3

import os
import requests
import json
import subprocess

releasesInfo = requests.get(
    'https://api.github.com/repos/haskell/haskell-language-server/releases').content

g = json.loads(releasesInfo)

for i in range(0, len(g[0]['assets'])-1):
    g[0]['assets'][i]['browser_download_url'] = (
        g[0]['assets'][i]['browser_download_url'].replace(
            'https://github.com',
            'https://download.fastgit.org'
        )
    )

# dump json onto the _base_path
with open('releasesInfo.json', 'w') as releasesInfoFile:
    json.dump(g, releasesInfoFile, indent=4)
