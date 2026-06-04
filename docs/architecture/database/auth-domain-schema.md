# User

# Organization

# Membership

# Role

# Permission

# Subscription

# Credit Wallet

# Audit Log

# users

id UUID PK

email VARCHAR(255) UNIQUE

username VARCHAR(100) UNIQUE

first_name VARCHAR(100)

last_name VARCHAR(100)

avatar_url TEXT

is_active BOOLEAN

is_verified BOOLEAN

last_login_at TIMESTAMP

created_at TIMESTAMP

updated_at TIMESTAMP

deleted_at TIMESTAMP NULL
# ############
INDEX(email)

INDEX(username)

INDEX(created_at)

# user_security

id UUID PK

user_id FK users

password_hash

mfa_enabled BOOLEAN

mfa_secret TEXT

backup_codes JSONB

password_changed_at TIMESTAMP

failed_login_attempts INT

locked_until TIMESTAMP

created_at

updated_at

# oauth_accounts

id UUID PK

user_id FK users

provider

provider_user_id

provider_email

created_at

# refresh_tokens

id UUID PK

user_id FK users

token_hash

expires_at

revoked_at

created_at

# 
INDEX(user_id)

INDEX(expires_at)

# organizations

id UUID PK

name VARCHAR(255)

slug VARCHAR(255) UNIQUE

owner_id FK users

logo_url TEXT

description TEXT

created_at

updated_at

deleted_at

# memberships

id UUID PK

organization_id FK organizations

user_id FK users

role_id FK roles

status VARCHAR(50)

joined_at TIMESTAMP

created_at

# Unique Constraint:
(organization_id, user_id)

# invitations

id UUID PK

organization_id

email

role_id

invited_by

expires_at

accepted_at

created_at

# permissions

id UUID PK

resource

action

created_at

# (role_id, permission_id)

# plans

id UUID PK

name

monthly_price

yearly_price

monthly_credits

max_team_members

max_projects

max_storage_gb

priority_queue BOOLEAN

commercial_license BOOLEAN

created_at

# subscriptions

id UUID PK

organization_id

plan_id

status

billing_cycle

started_at

expires_at

cancelled_at

created_at

# credit_wallets

id UUID PK

organization_id UNIQUE

balance BIGINT

created_at

updated_at

# credit_transactions

id UUID PK

wallet_id

amount

transaction_type

reference_id

description

created_at

# audit_logs

id UUID PK

organization_id

user_id

event_type

resource_type

resource_id

metadata JSONB

ip_address

user_agent

created_at

# #
User
│
├── UserSecurity
├── OAuthAccount
├── RefreshToken
│
└───────────────┐
                │
                ▼
          Membership
                │
                ▼
         Organization
                │
      ┌─────────┼─────────┐
      ▼         ▼         ▼
 Subscription Wallet AuditLog
      │
      ▼
     Plan

Role
 │
 ▼
RolePermission
 │
 ▼
Permission