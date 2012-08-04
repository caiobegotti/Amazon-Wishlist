var aAsc = [];
function sortTable(nr) {
	aAsc[nr] = aAsc[nr]=='asc'?'desc':'asc';
	$('table#livefilter-list>tbody>tr').tsort('td:eq('+nr+')', {order:aAsc[nr]});
}
