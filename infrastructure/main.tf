provider "google" {
  project = "your-gcp-project-id"
  region  = "us-central1"
}

# Create a Cloud Storage bucket
resource "google_storage_bucket" "my_bucket" {
  name     = "my-unique-bucket-name"  # Replace with a unique bucket name
  location = "US"
}

# Create a Vertex AI Gemini endpoint
resource "google_vertex_ai_endpoint" "gemini_endpoint" {
  name         = "gemini-endpoint"
  display_name = "Gemini Endpoint"
  location     = "us-central1"
}

# Create a VM instance
resource "google_compute_instance" "my_vm" {
  name         = "my-vm-instance"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"
    }
  }

  network_interface {
    network = "default"
    access_config {
      # Ephemeral IP
    }
  }

  service_account {
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}

# Output the bucket name, endpoint ID, and VM instance details
output "bucket_name" {
  value = google_storage_bucket.my_bucket.name
}

output "vertex_ai_endpoint_id" {
  value = google_vertex_ai_endpoint.gemini_endpoint.id
}

output "vm_instance_name" {
  value = google_compute_instance.my_vm.name
}