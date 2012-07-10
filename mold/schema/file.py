common = {
    'kind': {
        'type': 'string',
        'required': True,
        'pattern': 'file',
        'description': 'Indicates that this is a file resource',
    },
    'path': {
        'type': 'string',
        'required': True,
        'description': 'Absolute path name of file',
    },
}
obs_pre_common = {
    'owner': {
        'type': 'string',
        'description': "Name of the user owning the file",
    },
    'group': {
        'type': 'string',
        'description': "Name of the group owning the file",
    },
}

#------------------------------------------------------------------------------
# inspection
#------------------------------------------------------------------------------
inspection = {
    'type': 'object',
    'properties': common.copy(),
}


#------------------------------------------------------------------------------
# observation
#------------------------------------------------------------------------------
observation = {
    'type': 'object',
    'properties': common.copy(),
}
observation['properties'].update({
    'size': {
        'type': 'integer',
        'description': 'Current file size in bytes',
    },
    'sha': {
        'type': 'string',
        'description': ("SHA1 hash of the file's contents as a hexadecimal "
                        "string"),
    },
    'exists': {
        'type': 'boolean',
        'description': "``true`` if the file exists, ``false`` if it doesn't",
    }
})
observation['properties'].update(obs_pre_common)

#------------------------------------------------------------------------------
# prescription
#------------------------------------------------------------------------------
prescription = {
    'type': 'object',
    'properties': common.copy(),
}
prescription['properties'].update({
    'exists': {
        'type': 'boolean',
        'description': ("``true`` if the file should exist, ``false`` if it "
                        "should not exist"),
    }
})
prescription['properties'].update(obs_pre_common)


#------------------------------------------------------------------------------
schema = {
    'inspection': inspection,
    'observation': observation,
    'prescription': prescription,
}
