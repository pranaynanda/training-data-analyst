# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
import logging
import os
project_id = os.getenv('GCLOUD_PROJECT')

# TODO: Load the Cloud Pub/Sub module

from google.cloud import pubsub_v1

# END TODO

# TODO: Create a Pub/Sub Subscriber Client

sub_client = pubsub_v1.SubscriberClient()

# END TODO

# TODO: Create a Subscription object named worker-subscription

sub_path = sub_client.subscription_path(project_id, 'worker-subscription')

# END TODO
"""pull_feedback

Starts pulling messages from subscription
- receive callback function from calling module
- initiate the pull providing the callback function
"""


def pull_feedback(callback):
    # TODO: Subscriber to the worker-subscription,
    # invoking the callback

    sub_client.subscribe(sub_path, callback=callback)

    # END TODO
