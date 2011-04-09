#
# Copyright 2011 Shopzilla.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this 1 except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = True
    map.explicit = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE

    # Route root url
    map.connect('/', controller='view')

	# Make default
    map.redirect("/view", "/", _redirect_code='301 Moved Permanently')
    map.redirect("/view/index", "/", _redirect_code='301 Moved Permanently')

    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')
    
	
    return map
