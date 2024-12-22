 // Preview image before upload
        document.getElementById('photo').addEventListener('change', function(e) {
            const photoPreview = document.getElementById('photoPreview');
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    photoPreview.src = e.target.result;
                    photoPreview.classList.remove('d-none');
                }
                reader.readAsDataURL(file);
            }
        });