#!/bin/bash
if [ -z "$VIRTUAL_ENV" ]; then
    echo "You need to run this install a virtualenv"
    exit 1
fi

pip install -r install/requirements.txt



<<COMMENT1
#node deps

[buildout]
extends = buildout.cfg

parts += nodejs
  nodejs-bin
  npm
  mu
  opts
  pip
  streamlogger
  underscore

[nodejs]
recipe=zc.recipe.cmmi
url=http://nodejs.org/dist/node-v0.4.8.tar.gz #amd64
#url=http://nodejs.org/dist/node-v0.4.9.tar.gz

[nodejs-bin]
recipe=cns.recipe.symlink
symlink =
    node
    node-waf
symlink_base = ${buildout:parts-directory}/nodejs/bin/
symlink_target = ${buildout:bin-directory}

[pip]
recipe = gp.recipe.pip
virtualenv = .
install =


[activate]
# prioritize ${buildout:bin-directory} in environment variables
recipe=evg.recipe.activate

[npm]
recipe=collective.recipe.cmd
on_install=true
on_update=false
cmds=
    source ${buildout:bin-directory}/activate
    curl http://npmjs.org/install.sh | clean=yes sh
uninstall_cmds=
    ${buildout:bin-directory}/npm uninstall npm -g

[npm-bin]
recipe=collective.recipe.cmd
on_install=true
on_update=true
cmds=
    rm ${buildout:bin-directory}/npm*
    for f in `grep '#!' ${buildout:directory}/lib/node_modules/npm/bin/* -l`;do
        sed -i 's|/usr/bin/env node|${buildout:bin-directory}/node|' $f
    done
    ln -s ${buildout:directory}/lib/node_modules/npm/bin/npm.js ${buildout:bin-directory}/npm


[mu]
recipe=collective.recipe.cmd
on_install=true
on_update=true
cmds=
    ${buildout:bin-directory}/npm -g install mu
#uninstall_cmds=
#    ${buildout:bin-directory}/npm -g uninstall mu

[opts]
recipe=collective.recipe.cmd
on_install=true
on_update=true
cmds=
    ${buildout:bin-directory}/npm -g install opts

[streamlogger]
recipe=collective.recipe.cmd
on_install=true
on_update=true
cmds=
    ${buildout:bin-directory}/npm  -g install streamlogger

[underscore]
recipe=collective.recipe.cmd
on_install=true
on_update=true
cmds=
    ${buildout:bin-directory}/npm  -g install underscore
#uninstall_cmds=
#    ${buildout:bin-directory}/npm -g uninstall underscore

COMMENT1