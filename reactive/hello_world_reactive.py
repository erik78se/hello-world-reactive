from charms.reactive import when, when_not, set_state, is_state, hook, remove_state
from charmhelpers.core.hookenv import status_set

@hook('install')
def install():

    status_set('maintenance', 'Installing...')

    set_state('hello-world-reactive.installed')

@hook('start')
def start():

    status_set('maintenance', 'Starting...')

    set_state('hello-world-reactive.started')

    remove_state('hello-world-reactive.stopped')


@hook('config-changed')
def config_changed():
    
    status_set('maintenance', 'Changing config...')
    

@hook('update-status')
def config_changed():

    pass


@hook('leader-elected')
def leader_elected():

    pass


@hook('stop')
def stop():
    
    status_set('maintenance', 'Stopping...')
    set_state('hello-world-reactive.stopped')
    remove_state('hello-world-reactive.started')


@when('hello-world-reactive.started')
def started():

    # Handle the "hello-world-reactive.started" state
    
    status_set('active', 'I am started.')


@when('hello-world-reactive.stopped')
def stopped():

    # Handle the "hello-world-reactive.stopped" state
    
    status_set('waiting', 'I am stopped.')
