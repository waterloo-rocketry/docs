Minerva Developer Guide
=======================

.. note::

   This guide is based on the original Minerva documentation in Google Docs:

   - `Minerva Developer Reference <https://docs.google.com/document/d/1vz9b3J8ghjsyqJtUuTTT1KHH7F9GhhCrGC5Nmy-X3rQ>`__
   - `Developer Onboarding <https://docs.google.com/document/d/1otYHtmFHzkN8g7089EGQpxi9-7C_iKFhDt2L2tuwxHs>`__

This document is for **developers** who want to hack on the *minerva‑rewrite* Slackbot.  It combines the *Developer Onboarding* and *Developer Reference* PDFs.

.. contents:: Table of Contents
   :depth: 2
   :local:

1. Getting Access
-----------------

Development Slack Workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* URL : ``https://waterloorocketrydev.slack.com``
* Join via the *Development Slack Invite* pinned in **#software** or by DMing a contributor.
* Messages older than **90 days** disappear due to free tier.

Development Google Calendar
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Calendar ID: ``uwaterloo.rocketry.dev@gmail.com``.
* Request *“Make changes to events”* permission from the Software Lead.

Oracle Cloud Instance
^^^^^^^^^^^^^^^^^^^^^

* Shape **VM.Standard.A1.Flex** - 4 vCPU, 24 GiB RAM .
* Public IP: ``129.153.48.52``.
* Runs two **PM2** apps: ``minerva`` (prod) and ``minerva-dev`` (dev).
* To grant access, add the developer's SSH public key to ``~/.ssh/authorized_keys``.

Slack Apps
^^^^^^^^^^

* **minerva** - production, **minerva-dev** - development.
* Add collaborators via *Settings → Collaborators*; production access only for trusted devs.

Optional Development Google Account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Credentials for ``uwaterloo.rocketry.dev@gmail.com`` are available in **#accounts** (ask lead).


2. Local Setup
--------------

Clone and bootstrap :

::

   git clone https://github.com/waterloo-rocketry/minerva-rewrite
   cd minerva-rewrite
   # Install Node ≥ 18 LTS and Yarn or pnpm
   cp .env.example .env  # fill with dev secrets (see below)
   yarn install
   yarn start            # run locally


3. Deployment Workflow
----------------------

Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* GitHub Actions builds → SSHes into Oracle VM → swaps artefact.
* Branch **development** → auto-deploys to dev workspace.
* Branch **main** → auto-deploys to production after PR merge.

Local Testing 
^^^^^^^^^^^^^

Run ``yarn start`` locally.  Avoid port clashes with the dev bot in Oracle Cloud; ensure your local ``.env`` uses dev tokens.

Deploy to Development
^^^^^^^^^^^^^^^^^^^^^

Force-push to **development** *or* execute::

   yarn deploy-dev

Deploy to Production
^^^^^^^^^^^^^^^^^^^^

Merge PR → Actions run tests → deployment to prod Slack.

Viewing Logs
^^^^^^^^^^^^

::

   ssh ubuntu@129.153.48.52
   pm2 list
   pm2 logs minerva        # production
   pm2 logs minerva-dev    # development


4. Environment Variables
------------------------

Both dev and prod use these variables.

.. list-table:: Environment Variables
   :header-rows: 1
   :widths: 25 75

   * - Variable
     - Where to Get / Notes
   * - ``GOOGLE_ACCOUNT_CLIENT``  
       ``GOOGLE_ACCOUNT_SECRET``
     - Google Cloud Console → *Credentials* of  
       • Production: *waterloorocketry-minerva* project.  
       • Dev: *rocketry-minerva* project.
   * - ``GOOGLE_ACCOUNT_TOKEN``
     - Generate new refresh token via Google OAuth  
       Playground; scope ``calendar.events``.
   * - ``GOOGLE_ACCOUNT_OAUTH_REDIRECT``
     - Typically ``https://developers.google.com/oauthplayground/``.
   * - ``SLACK_APP_TOKEN``  
       ``SLACK_OAUTH_TOKEN``  
       ``SLACK_SIGNING_SECRET``
     - Slack API → *Basic Information → App-Level Tokens*  
       Slack API → *OAuth & Permissions*   
       Slack API → *Basic Information → App Credentials*
   * - ``NODE_ENV``
     - ``production`` or ``development`` to toggle runtime  
       settings .
   * - ``DEPLOY_COMMIT_SHA``
     - Auto-injected by GitHub Actions at deploy.

5. SSH Quick Commands
---------------------

::

   # Restart dev bot safely
   pm2 restart minerva-dev

   # Tail last 200 lines
   pm2 logs minerva --lines 200

6. Onboarding Checklist
-----------------------

- Add dev to Development Slack.

- Grant *Make changes to events* on Dev Calendar.

- Add their SSH key to Oracle VM.

- Provide ``.env`` dev secrets (DM or scp from server).

- (Optional) Add as collaborator to **minerva-dev** Slack App.

