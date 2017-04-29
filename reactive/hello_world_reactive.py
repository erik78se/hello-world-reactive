from charms.reactive import when, when_not, set_state, is_state, hook, remove_state
from charmhelpers.core.hookenv import status_set, config
from charmhelpers.core.host import is_container


@hook('install')
def install_handler():

    # Set the user defined "installing" state when this hook event occurs.
    
    set_state('hello-world-reactive.installing')

@hook('start')
def start_handler():

    # Set the user defined "starting" state when this hook event occurs.
    
    set_state('hello-world-reactive.starting')

@hook('stop')
def stop_handler():

    # Set the user defined "stopping" state when this hook event occurs.
    
    set_state('hello-world-reactive.stopping')
    

@hook('config-changed')
def config_changed_handler():

    # We could set the user defined "config-changed" state and do this just like
    # the start, install, stop handlers. But we leave this up to a reader to complete.
    
    pass
    

@hook('update-status')
def update_status_handler():

    # We could set the user defined "update-status" state and do this just like
    # the start, install, stop handlers. But we leave this up to a reader to complete.

    pass


@hook('leader-elected')
def leader_elected_handler():
    
    # We could set the user defined "leader-elected" state and do this just like
    # the start, install, stop handlers. But we leave this up to a reader to co
    
    pass


@when('hello-world-reactive.installing')
def install_handler():
    
    status_set('maintenance', 'Installing...')
    
    # Handle the startup of the application
    
    status_set('active', 'I am installing.')
    
    # Remove the state "installing" since we are done.
    
    remove_state('hello-world-reactive.installing')
    

@when('hello-world-reactive.starting')
def start_handler():

    status_set('maintenance', 'Starting...')

    # Handle the start of the application
    
    cfg = config()

    # Get the value for the "message" key.

    m = cfg.get('message')
    
    status_set('active', ("Started with message: %s" % m))

    # Remove the "starting" state since we are done.

    remove_state('hello-world-reactive.starting')

    
@when('hello-world-reactive.stopping')
def stop_handler():

    status_set('maintenance', 'Stopping...')

    # Handle the stop sequence of the application
    
    status_set('active', 'I am stopping.')

    # Remove the "stopping" state since we are done.
        
    remove_state('hello-world-reactive.stopping')
