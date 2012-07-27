common = {
    'kind': {
        'type': 'string',
        'required': True,
        'pattern': 'user',
        'description': 'Indicates that this is a user resource',
    },
    'name': {
        'type': 'string',
        'required': True,
        'description': 'Name of user',
    },
}

o_p_common = {
    'shell': {
        'type': 'string',
        'description': 'Path to the shell for user',
    },
    'password': {
        'type': 'string',
        'description': 'Password hash',
    },
    'uid': {
        'type': 'string',
        'description': "User's user ID",
    },
    'gid': {
        'type': 'string',
        'description': "User's group ID or name",
    },
    'home': {
        'type': 'string',
        'description': "Path to user's home",
    },
    'comment': {
        'type': 'string',
        'description': "A description of the user",
    },
}


#------------------------------------------------------------------------------
# identity
#------------------------------------------------------------------------------
identity = {
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
    'exists': {
        'type': 'boolean',
        'required': True,
        'description': "true if the user exists; false if it doesn't",
    }
})
observation['properties'].update(o_p_common)

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
        'required': True,
        'description': ("true if the user should exist; false if it "
                        "should not exist"),
    }
})
prescription['properties'].update(o_p_common)


#------------------------------------------------------------------------------
schema = {
    'identity': identity,
    'observation': observation,
    'prescription': prescription,
}
