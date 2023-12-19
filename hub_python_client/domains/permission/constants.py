from enum import Enum

class PermissionKey(Enum):
    ADMIN_UI_USE = 'admin_ui_use'
    PROPOSAL_ADD = 'proposal_add'
    PROPOSAL_DROP = 'proposal_drop'
    PROPOSAL_EDIT = 'proposal_edit'
    PROPOSAL_APPROVE = 'proposal_approve'
    REGISTRY_MANAGE = 'registry_manage'
    REGISTRY_PROJECT_MANAGE = 'registry_project_manage'
    STATION_ADD = 'station_add'
    STATION_DROP = 'station_drop'
    STATION_EDIT = 'station_edit'
    TRAIN_APPROVE = 'train_approve'
    TRAIN_EDIT = 'train_edit'
    TRAIN_ADD = 'train_add'
    TRAIN_EXECUTION_START = 'train_execution_start'
    TRAIN_EXECUTION_STOP = 'train_execution_stop'
    TRAIN_DROP = 'train_drop'
    TRAIN_RESULT_READ = 'train_result_read'
    MASTER_IMAGE_MANAGE = 'master_image_manage'
    MASTER_IMAGE_GROUP_MANAGE = 'master_image_group_manage'
    SERVICE_MANAGE = 'service_manage'

# todo add PermissionID AuthPermissionName form authhub missing
# todo add PermissionIDType AuthPermissionNameType form authhub missing
