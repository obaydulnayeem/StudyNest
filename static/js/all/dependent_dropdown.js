// UNIVERSITY CHOICE DROPDOWN
$("#id_university_type").change(function () {
    const url = $("#QuestionForm").attr("data-universities-url");
    const universityTypeId = $(this).val();

    $.ajax({
        url: url,
        data: {
            'university_type_id': universityTypeId 
        },
        success: function (data) {
            $("#id_university").html(data);
        }
    });

});


// FACULTY CHOICE DROPDOWN
$("#id_university").change(function () {
    const url = $("#QuestionForm").attr("data-faculties-url");
    const universityId = $(this).val();
    $.ajax({
        url: url,
        data: {
            'university_id': universityId 
        },
        success: function (data) {  
            $("#id_faculty").html(data);
        }
    });
});


// DEPARTMENT CHOICE DROPDOWN
// $("#id_university, #id_faculty").change(function () {
//     const url = $("#QuestionForm").attr("data-departments-url");
//     const universityId = $("#id_university").val();
//     const facultyId = $("#id_faculty").val();
//     $.ajax({
//         url: url,
//         data: {
//             'university_id': universityId,
//             'faculty_id': facultyId
//         },
//         success: function (data) {
//             $("#id_department").html(data);
//         }
//     });
// });


// // COURSE CHOICE DROPDOWN
// $("#id_university, #id_department, #id_year, #id_semester").change(function () {
//     const url = $("#QuestionForm").attr("data-courses-url");
//     const universityId = $("#id_university").val();
//     const departmentId = $("#id_department").val();
//     const year = $("#id_year").val();
//     const semester = $("#id_semester").val();

//     $.ajax({
//         url: url,
//         data: {
//             'university_id': universityId,
//             'department_id': departmentId,
//             'year': year,
//             'semester': semester
//         },
//         success: function (data) {
//             $("#id_course").html(data);
//         }
//     });
// });


// COURSE CHOICE DROPDOWN
$("#id_semester").change(function () {
    const url = $("#QuestionForm").attr("data-courses-url");
    // const year = $("#id_year").val();
    const semester = $("#id_semester").val();

    $.ajax({
        url: url,
        data: {
            // 'year': year,
            'semester': semester
        },
        success: function (data) {
            $("#id_course").html(data);
        }
    });
});

// TEACHER CHOICE DROPDOWN
// $("#id_university, #id_department").change(function () {
// const url = $("#QuestionForm").attr("data-teachers-url");
// const universityId = $("#id_university").val();
// const departmentId = $("#id_department").val();

// $.ajax({
//     url: url,
//     data: {
//         'university_id': universityId,
//         'department_id': departmentId,
//     },
//     success: function (data) {
//         $("#id_teacher").html(data);
//     }
// });
// });

