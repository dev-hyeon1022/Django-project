// var $prev = $($(".page-button")[0]);

// $(".page-button").each((i, e) => {
// 	var $pageNumber = $(e);
//
// 	$pageNumber.on("click", function (e) {
// 		e.preventDefault();
// 		if ($prev == $pageNumber) {
// 			return;
// 		}
//
// 		$prev.removeClass("page-button-active");
// 		$pageNumber.addClass("page-button-active");
//
// 		$prev = $pageNumber;
// 	});
// });


//
/*체크 된 게시물의 번호 가져오기*/
const $checkBoxs = $("input[type=checkbox]");
const $deleteButton = $(".delete-button");


$deleteButton.on("click", function (e) {
	let postIdArr = [];

	$checkBoxs.each((i, checkBox) => {
		id = $(checkBox).parent().siblings(".noticeId").text()
		if ($(checkBox).prop("checked") && id!=='') {
			postIdArr.push(id);
		}
	})
	if (postIdArr) {
		confirm(postIdArr + "번을 삭제하시겠습니까?");
	} else {
		confirm("공지사항 게시글을 선택해주세요.");
	}
	adminNoticeService.remove(postIdArr);
});

const adminNoticeService = (function () {
	function remove(postIdArr) {
		fetch("/administrator/board/notice/delete/", {
			method: 'post',
			headers: {'Content-Type': 'application/json; charset=utf-8'},
			body: JSON.stringify({post_ids: postIdArr})
		}).then(()=>{
			location.reload();
		});

	}

	return { remove: remove }
})();

// 검색
$(".search-button img").on('click', ()=>{
	keyword = $(".search-box").val();
	location.href = keyword === "" ? "/administrator/board/notice/list/" : `/administrator/board/notice/list/${keyword}/`;
})
