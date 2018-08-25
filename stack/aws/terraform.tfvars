//local developer testing
environment = "local"
vpc_cidr = "10.0.0.0/16"
public_subnet_cidrs = ["10.0.0.0/24", "10.0.1.0/24", "10.0.2.0/24"]
availability_zones = ["ap-southeast-1a", "ap-southeast-1b", "ap-southeast-1c"]
short_availability_zones = ["1a", "1b", "1c"]
az_index = "0"
max_size = "1"
min_size = "5"
desired_capacity = "1"
instance_type = "t2.nano"
pg_end_point = ""
pg_instance_class = "db.t2.micro"
pg_allocated_storage = "20"
pg_username = "ngip_user"
pg_password = "ngip_user"
pg_vpc_security_group_ids = ""
pg_subnet_id = ""
pg_version = "9.6.9"
pg_parameter_group = "9.6"
pg_snapshot_identifier = "general-2018-08-22-03-52"
pg_monitoring_interval = "15"
pg_backup_retention_period = "0"
pg_backup_window = "21:30-22:00"
