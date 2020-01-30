var loc = window.location;
var base_url = window.location.href.split("?")[0];
var server_url = "" + loc.protocol + "//" + loc.host + '/';


// Display Vehicle listing in vendor view

$(document).ready(function ($) {
    $(document).on('click', '.vehicle_listing', function () {
        $.noConflict();
        var formData = {
            'vendor_id': $('#vendor_id').val()
          }
        $('#example').DataTable({
            "processing": true,
            "bRetrieve": true,
            "paging": true,
            "lengthMenu": [ [10, 25, 50, 100, -1], [10, 25, 50, 100, "All"] ],
            "pageLength": 7,
            "ajax": {
                method: "POST",
                data : formData,
                "processing": true,
                "url": server_url + 'admin/get-vehicle/',
                "dataSrc": "",
                dataType: "JSON",
                cache: false
            },
   
            "columns": [
                { "data": 'vehicle_no' },
                { "data": 'mileage' },
                { "data": 'chassis_no' },
                { "data": 'status' },
                {"mRender": function ( data, type, row ) {
                    return "<a href='javascript:void(0);' class='delete-vehicle' data-vendor-id="+row.vendor+"><i class='fa fa-trash' aria-hidden='true'></i></a>"
                }
            }

            ]
        });
    });
});

$(document).on('click','.delete-vehicle',function(){
    if (confirm("Are you sure?")) {
        vendor_id = $(this).attr("data-vendor-id");
    }
    return false;    
})